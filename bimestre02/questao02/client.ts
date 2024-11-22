import axios from 'axios';

const API_URL = "http://127.0.0.1:5000";

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
    const nickname = "astrologoCanadense"; // Substitua pelo nickname desejado
    const sign = "aries"; // Substitua pelo signo desejado

    // const nickname2 = "astrologoCanadense666"; // Substitua pelo nickname desejado
    // const sign2 = "sagitario"; // Substitua pelo signo desejado

    const plan1 = await login(nickname);
    // const plan2 = await login(nickname2)
    if (plan1) {
        await getHoroscope(nickname, sign);
    }

    // if(plan2){
    //     await getHoroscope(nickname2, sign2);
    // }
})();
