import axios from "axios"
const BASE_URL=import.meta.env.VITE_NEWS_API_URL
const BASE_API_KEY=import.meta.env.VITE_NEWS_API_KEY

export const getNews = async () => {
    try {
        const response = await axios.get(`${BASE_URL}latest-news`,{
            params: {
                apiKey: BASE_API_KEY
            }
        })
        return response.data
    } catch (error) {
        console.log(error)
    }
}