import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-government-scheme-advisor-33ecvqabg-tamnurunithins-projects.vercel.app/",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
