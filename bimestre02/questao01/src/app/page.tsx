'use client'

import { useState, useEffect, } from "react"
import * as React from "react"
import { Button, buttonVariants } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { CircleDollarSign } from 'lucide-react';
import Link from 'next/link';

// export default function Component() {
//   const [real, setReal]: any = useState<string>("")
//   const [iene, setIene]: any = useState<string>("")
//   const [euro, setEuro]: any = useState<string>("")

//   useEffect(()=>{
//     fetch("https://v6.exchangerate-api.com/v6/e8de14610a301964d72aa22a/latest/USD")
//     .then((response)=> {if (!response.ok) {
//       throw new Error('Network response was not ok');
//     } return response.json()})
//     .then((json)=>setReal(json.conversion_rates.BRL))
//     .catch((err)=> console.log(err))
//   },[])

//   useEffect(()=>{
//     fetch("https://v6.exchangerate-api.com/v6/e8de14610a301964d72aa22a/latest/USD")
//     .then((response)=> {return response.json()})
//     .then((data)=>setEuro(data.conversion_rates.EUR))
//     .catch((err)=> console.log(err))
//   },[])

//   useEffect(()=>{
//     fetch("https://v6.exchangerate-api.com/v6/e8de14610a301964d72aa22a/latest/USD")
//     .then((response)=> {return response.json()})
//     .then((data)=>setIene(data.conversion_rates.JPY))
//     .catch((err)=> console.log(err))
//   },[])

//   const currencies = [
//     { name: 'Real (BRL)', value: real },
//     { name: 'Euro (EUR)', value: euro },
//     { name: 'Iene (JPY)', value: iene },
//   ]

//   return (
//     <div className="min-h-screen bg-black text-white overflow-hidden">
//       <div className="relative z-10">
//         <div
//           className="fixed inset-0 bg-[radial-gradient(circle_800px_at_50%_400px,#00ff8a15,#00ff8a00_80%),radial-gradient(circle_800px_at_80%_400px,#ff000015,#ff000000_80%),radial-gradient(circle_800px_at_20%_400px,#0000ff15,#0000ff00_80%)]"
//           aria-hidden="true"
//         />
//         <main className="relative">
//           <div className="container mx-auto px-6 pt-16 pb-32 text-center">
//             <h1 className="mx-auto max-w-4xl text-4xl font-bold tracking-tight sm:text-4xl lg:text-5xl">
//               Confira aqui algumas cotações de destaque
//             </h1>
//    <Card className="w-[700px]">
//     <CardHeader>
//     <CardTitle>Cotações</CardTitle>
//   </CardHeader>
//   <CardContent>
//     <ul className="space-y-4 pt-4">
//           {currencies.map((currency) => (
//             <li key={currency.name} className="flex justify-between items-center border-b pt-4 pb-4">
//               <span className="font-medium">{currency.name}</span>
//               <span className="text-lg"> {currency.value}</span>
//             </li>
//           ))}
//         </ul>
//   </CardContent>
//   <CardFooter className="flex justify-between">
//     <Link href="https://ui.shadcn.com/docs/components/button" className={buttonVariants({ variant: "outline" })}>
//       <CircleDollarSign/> Mais Cotações
//     </Link>
//   </CardFooter>
// </Card>
//           <div>
//           <h2 className="text-2xl mb-4">  </h2>
//           <ul className="space-y-4 pt-4">
//               {currencies.map((currency) => (
//                 <li key={currency.name} className="flex justify-between items-center border-b pt-4 pb-4">
//                   <span className="font-medium">{currency.name}</span>
//                   <span className="text-lg"> {currency.value}</span>
//                 </li>
//               ))}
//             </ul>
//           </div>
//           </div>
//         </main>
//       </div>
//     </div>
//   )
// }



export default function CardWithForm() {

  const [real, setReal]: any = useState<string>("")
  const [iene, setIene]: any = useState<string>("")
  const [euro, setEuro]: any = useState<string>("")

  useEffect(() => {
    fetch("https://v6.exchangerate-api.com/v6/e8de14610a301964d72aa22a/latest/USD")
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        } return response.json()
      })
      .then((json) => setReal(json.conversion_rates.BRL))
      .catch((err) => console.log(err))
  }, [])

  useEffect(() => {
    fetch("https://v6.exchangerate-api.com/v6/e8de14610a301964d72aa22a/latest/USD")
      .then((response) => { return response.json() })
      .then((data) => setEuro(data.conversion_rates.EUR))
      .catch((err) => console.log(err))
  }, [])

  useEffect(() => {
    fetch("https://v6.exchangerate-api.com/v6/e8de14610a301964d72aa22a/latest/USD")
      .then((response) => { return response.json() })
      .then((data) => setIene(data.conversion_rates.JPY))
      .catch((err) => console.log(err))
  }, [])

  const currencies = [
    { name: 'Real (BRL)', value: real },
    { name: 'Euro (EUR)', value: euro },
    { name: 'Iene (JPY)', value: iene },
  ]

  return (
    <div className="min-h-screen bg-black text-white overflow-hidden">
      <div className="relative z-10">
        <div
          className="fixed inset-0 bg-[radial-gradient(circle_800px_at_50%_400px,#00ff8a15,#00ff8a00_80%),radial-gradient(circle_800px_at_80%_400px,#ff000015,#ff000000_80%),radial-gradient(circle_800px_at_20%_400px,#0000ff15,#0000ff00_80%)]"
          aria-hidden="true"
        />
        <main className="relative">
          <div className="container mx-auto px-6 pt-16 pb-32 text-center">
            <h1 className="mx-auto max-w-4xl text-4xl font-bold tracking-tight sm:text-4xl lg:text-5xl">
              Confira aqui algumas cotações de destaque
            </h1>
            <div className="flex items-center justify-center space-y-4 pt-12">
              <Card className="w-[700px] space-y-4 pt-4 bg-white/10 backdrop-blur-md border-white/20 shadow-lg text-white ">
                <CardHeader>
                  <CardTitle className="mx-auto max-w-4xl text-4xl font-bold tracking-tight sm:text-4xl lg:text-2.5xl">Cotações</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-4 pt-4">
                    {currencies.map((currency) => (
                      <li key={currency.name} className="flex justify-between items-center border-b pt-4 pb-4">
                        <span className="font-medium">{currency.name}</span>
                        <span className="text-lg"> {currency.value}</span>
                      </li>
                    ))}
                  </ul>
                </CardContent>
                <CardFooter className="flex justify-between text-white hover:black">
                  <Link href="https://www.xe.com/currencyconverter/" className={buttonVariants({ variant: "ghost" })}>
                    <CircleDollarSign /> Mais Cotações
                  </Link>
                  <Link href="https://www.exchangerate-api.com/" className={buttonVariants({ variant: "ghost" })}>
                    <CircleDollarSign /> API Utilizada
                  </Link>
                </CardFooter>
              </Card>
            </div>
            {/* <div>
          <h2 className="text-2xl mb-4">  </h2>
          <ul className="space-y-4 pt-4">
              {currencies.map((currency) => (
                <li key={currency.name} className="flex justify-between items-center border-b pt-4 pb-4">
                  <span className="font-medium">{currency.name}</span>
                  <span className="text-lg"> {currency.value}</span>
                </li>
              ))}
            </ul>
          </div> */}
          </div>
        </main>
      </div>
    </div>
    // <Card className="w-[700px]">
    //   <CardHeader>
    //     <CardTitle>Cotações</CardTitle>
    //   </CardHeader>
    //   <CardContent>
    //     <ul className="space-y-4 pt-4">
    //           {currencies.map((currency) => (
    //             <li key={currency.name} className="flex justify-between items-center border-b pt-4 pb-4">
    //               <span className="font-medium">{currency.name}</span>
    //               <span className="text-lg"> {currency.value}</span>
    //             </li>
    //           ))}
    //         </ul>
    //   </CardContent>
    //   <CardFooter className="flex justify-between">
    //     <Link href="https://ui.shadcn.com/docs/components/button" className={buttonVariants({ variant: "outline" })}>
    //       <CircleDollarSign/> Mais Cotações
    //     </Link>
    //   </CardFooter>
    // </Card>
  )
}
