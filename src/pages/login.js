const baseURL = process.env.REACT_APP_API_URL;

const handleLogin = async (username, password) => {
  try {
    const res = await fetch(`${baseURL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
      credentials: "include", // if using cookies or sessions
    });

    const data = await res.json();

    if (res.ok) {
      console.log("Login successful!", data);
    } else {
      console.error("Login failed:", data.message);
    }
  } catch (err) {
    console.error("Network error:", err);
  }
};
