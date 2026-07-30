import StatsGrid from '../components/StatsGrid';
import RevenueChart from '../components/RevenueChart';
import RecentOrders from '../components/RecentOrders';

export default function Dashboard() {
  return (
    <main className="dashboard">
      <h1>Organizer Dashboard</h1>
      <StatsGrid />
      <RevenueChart />
      <RecentOrders />
    </main>
  );
}
