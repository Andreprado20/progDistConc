// app/page.tsx
"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

const API_BASE_URL = "https://prog-dist-conc03.vercel.app/api";

type Entity = "usuarios" | "carteiras" | "criptoativos" | "carteira_cripto" | "transacoes";

interface FormData {
  [key: string]: string | number;
}

export default function Home() {
  const [activeTab, setActiveTab] = useState<Entity>("usuarios");
  const [data, setData] = useState<any[]>([]);
  const [formData, setFormData] = useState<FormData>({});
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [editId, setEditId] = useState<number | null>(null);

  useEffect(() => {
    fetchData(activeTab);
  }, [activeTab]);

  const fetchData = async (entity: Entity) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/${entity}`);
      setData(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      if (isEditing) {
        await axios.put(`${API_BASE_URL}/${activeTab}/${editId}`, formData);
      } else {
        await axios.post(`${API_BASE_URL}/${activeTab}`, formData);
      }
      fetchData(activeTab);
      setIsDialogOpen(false);
      setFormData({});
      setIsEditing(false);
      setEditId(null);
    } catch (error) {
      console.error("Error submitting data:", error);
    }
  };

  const handleDelete = async (id: number) => {
    try {
      await axios.delete(`${API_BASE_URL}/${activeTab}/${id}`);
      fetchData(activeTab);
    } catch (error) {
      console.error("Error deleting data:", error);
    }
  };

  const handleEdit = (item: any) => {
    setFormData(item);
    setIsEditing(true);
    setEditId(item.id);
    setIsDialogOpen(true);
  };

  const renderForm = () => {
    const fields: { [key in Entity]: string[] } = {
      usuarios: ["nome", "login", "senha"],
      carteiras: ["nome", "id_usuario"],
      criptoativos: ["nome", "codigo", "preco"],
      carteira_cripto: ["id_carteira", "id_criptoativo", "quantidade"],
      transacoes: ["id_carteira_origem", "id_carteira_destino", "id_criptoativo", "quantidade", "tipo"],
    };

    return (
      <form onSubmit={handleSubmit} className="space-y-4">
        {fields[activeTab].map((field) => (
          <div key={field}>
            <Label htmlFor={field}>{field}</Label>
            {field === "tipo" && activeTab === "transacoes" ? (
              <Select
                value={formData[field] as string}
                onValueChange={(value) => setFormData({ ...formData, [field]: value })}
              >
                <SelectTrigger>
                  <SelectValue placeholder="Select transaction type" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="compra">Compra</SelectItem>
                  <SelectItem value="venda">Venda</SelectItem>
                  <SelectItem value="transferencia">Transferência</SelectItem>
                </SelectContent>
              </Select>
            ) : (
              <Input
                id={field}
                value={formData[field] || ""}
                onChange={(e) => setFormData({ ...formData, [field]: e.target.value })}
                required
              />
            )}
          </div>
        ))}
        <Button type="submit">{isEditing ? "Update" : "Create"}</Button>
      </form>
    );
  };

  const renderTable = () => {
    if (data.length === 0) return <p>No data available.</p>;

    const columns = Object.keys(data[0]);

    return (
      <Table>
        <TableHeader>
          <TableRow>
            {columns.map((column) => (
              <TableHead key={column}>{column}</TableHead>
            ))}
            <TableHead>Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {data.map((item, index) => (
            <TableRow key={index}>
              {columns.map((column) => (
                <TableCell key={column}>{item[column]}</TableCell>
              ))}
              <TableCell>
                <Button variant="outline" size="sm" onClick={() => handleEdit(item)}>
                  Edit
                </Button>
                <Button
                  variant="destructive"
                  size="sm"
                  onClick={() => handleDelete(item.id)}
                  className="ml-2"
                >
                  Delete
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    );
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Crypto Wallet Manager</h1>
      <Tabs value={activeTab} onValueChange={(value) => setActiveTab(value as Entity)}>
        <TabsList>
          <TabsTrigger value="usuarios">Users</TabsTrigger>
          <TabsTrigger value="carteiras">Wallets</TabsTrigger>
          <TabsTrigger value="criptoativos">Crypto Assets</TabsTrigger>
          <TabsTrigger value="carteira_cripto">Wallet-Crypto</TabsTrigger>
          <TabsTrigger value="transacoes">Transactions</TabsTrigger>
        </TabsList>
        {["usuarios", "carteiras", "criptoativos", "carteira_cripto", "transacoes"].map((tab) => (
          <TabsContent key={tab} value={tab}>
            <Card>
              <CardHeader>
                <CardTitle className="flex justify-between items-center">
                  {tab.charAt(0).toUpperCase() + tab.slice(1)}
                  {tab !== "carteira_cripto" && (
                    <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
                      <DialogTrigger asChild>
                        <Button onClick={() => {
                          setFormData({});
                          setIsEditing(false);
                          setEditId(null);
                        }}>
                          Add New
                        </Button>
                      </DialogTrigger>
                      <DialogContent>
                        <DialogHeader>
                          <DialogTitle>{isEditing ? "Edit" : "Add New"} {tab.slice(0, -1)}</DialogTitle>
                        </DialogHeader>
                        {renderForm()}
                      </DialogContent>
                    </Dialog>
                  )}
                </CardTitle>
              </CardHeader>
              <CardContent>{renderTable()}</CardContent>
            </Card>
          </TabsContent>
        ))}
      </Tabs>
    </div>
  );
}