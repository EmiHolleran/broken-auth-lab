import API from "../api"; // or wherever your api.js is

const handleLogin = async () => {
  try {
    const response = await API.post("/login", {
      username: "testuser",
      password: "1234",
    });
    console.log("Login successful", response.data);
  } catch (err) {
    console.error("Login failed", err.response?.data || err.message);
  }
};
