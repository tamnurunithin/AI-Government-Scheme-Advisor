import axios from "axios";

const API = axios.create({
  baseURL: "https://ai-government-scheme-advisor-33ecvqabg-tamnurunithins-projects.vercel.app/",
});

export const askQuestion = async (question) => {
  const response = await API.post("/chat", {
    question,
  });

  return response.data;
};
