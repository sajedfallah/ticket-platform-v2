import { createBrowserRouter } from "react-router-dom";
import Dashboard from "../pages/Dashboard";
import Events from "../pages/Events";
import AdminLogin from "../pages/AdminLogin";
import CheckInScanner from "../pages/CheckInScanner";

export const router = createBrowserRouter([
  { path: "/login", element: <AdminLogin /> },
  { path: "/", element: <Dashboard /> },
  { path: "/events", element: <Events /> },
  { path: "/checkin", element: <CheckInScanner /> },
]);
