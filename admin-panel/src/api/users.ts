import api from './client';

export const getUsers = async () => {
  const response = await api.get('/users');
  return response.data;
};

export const updateUserRole = async (id: string, role: string) => {
  const response = await api.patch(`/users/${id}/role`, { role });
  return response.data;
};
