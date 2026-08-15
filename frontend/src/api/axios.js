import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-government-scheme-advisor-lai3.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
