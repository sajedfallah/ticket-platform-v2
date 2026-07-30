import api from './client';

export const getPayments = async () => {
  const response = await api.get('/payments');
  return response.data;
};

export const getRevenueSummary = async () => {
  const response = await api.get('/payments/summary');
  return response.data;
};
