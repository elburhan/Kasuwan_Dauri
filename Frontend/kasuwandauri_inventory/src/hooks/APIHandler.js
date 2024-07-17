import { useState } from "react";
import axios from 'axios';

function useApi() {
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const callApi = async ({ url, method = "GET", body = {}, headers = {} }) => {
    setLoading(true);
    setError("");
    let response = null;
    try {
      response = await axios.request({ url, method, data: body, headers });
    } catch (err) {
      setError(err.message || "An error occurred");
      throw err; // Re-throw the error to handle it in the calling function
    } finally {
      setLoading(false);
    }
    return response;
  };

  return { callApi, error, loading };
}

export default useApi;
