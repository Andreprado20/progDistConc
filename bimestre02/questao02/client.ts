import axios from 'axios';

const API_URL = "http://127.0.0.1:5000";


async function createUser(nickname: string, plan: string) {
    try {
        const response = await axios.post(`${API_URL}/create_user`, { nickname, plan });
        if (response.data.success) {
            console.log(response.data.message);
        } else {
            console.error(response.data.message);
        }
    } catch (error) {
        console.error("Erro ao conectar ao servidor para criar usuário:");
    }
}

async function login(nickname: string) {
    try {
        const response = await axios.post(`${API_URL}/login`, { nickname });
        if (response.data.success) {
            console.log(`Login bem-sucedido! Plano: ${response.data.plan}`);
            return response.data.plan;
        } else {
            console.error(response.data.message);
            return null;
        }
    } catch (error) {
        console.error("Erro ao conectar ao servidor:");
        return null;
    }
}

async function getHoroscope(nickname: string, sign: string) {
    try {
        const response = await axios.post(`${API_URL}/horoscope`, { nickname, sign });
        if (response.data.success) {
            console.log("Horóscopo do dia:", response.data.data);
        } else {
            console.error(response.data.message);
        }
    } catch (error) {
        console.error("Erro ao conectar ao servidor:");
    }
}

(async () => {
    const newNickname = "estrelaNova";
    const newPlan = "advanced";
    await createUser(newNickname, newPlan);
    const plan = await login(newNickname);
    if (plan) {
        const sign = "aries"; 
        await getHoroscope(newNickname, sign);
        }
    }
)();

(async ()=>{
    const nickname = "astrologoCanadense"; 
    const sign = "aries"; 
    const plan1 = await login(nickname);
    if (plan1) {
        await getHoroscope(nickname, sign);
    }
})();
