import client from './client';

export async function getDashboardStats(){
  const response = await client.get('/dashboard/stats');
  return response.data;
}

export async function getRecentOrders(){
  const response = await client.get('/dashboard/orders/recent');
  return response.data;
}
