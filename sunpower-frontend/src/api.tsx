import axios from "axios";

const API_BASE = "http://localhost:8000";

// Calls the backend calculation you already built
export async function getNetEmissions(
  companyId: number,
  from: string,
  to: string
) {
  const res = await axios.get(
    `${API_BASE}/companies/${companyId}/net-emissions`,
    { params: { date_from: from, date_to: to } }
  );

  return res.data;
}
