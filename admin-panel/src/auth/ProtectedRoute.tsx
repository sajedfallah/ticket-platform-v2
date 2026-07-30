import React from 'react';

interface Props {
  children: React.ReactNode;
  roles?: string[];
}

export default function ProtectedRoute({ children, roles = [] }: Props) {
  const user = JSON.parse(localStorage.getItem('admin_user') || 'null');

  if (!user) {
    return <div>Unauthorized</div>;
  }

  if (roles.length && !roles.includes(user.role)) {
    return <div>Access denied</div>;
  }

  return <>{children}</>;
}
