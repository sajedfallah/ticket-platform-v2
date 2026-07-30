import { createBrowserRouter } from "react-router-dom";
import Home from "../pages/Home";
import Events from "../pages/Events";
import EventDetails from "../pages/EventDetails";
import Checkout from "../pages/Checkout";
import Tickets from "../pages/Tickets";
import Profile from "../pages/Profile";

export const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  { path: "/events", element: <Events /> },
  { path: "/events/:id", element: <EventDetails /> },
  { path: "/checkout", element: <Checkout /> },
  { path: "/tickets", element: <Tickets /> },
  { path: "/profile", element: <Profile /> },
]);
