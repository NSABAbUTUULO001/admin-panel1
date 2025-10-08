"use client"

import { useEffect } from "react"
import { CRMDashboard } from "@/components/crm-dashboard"

export default function DashboardPage() {
  useEffect(() => {
    const token = localStorage.getItem("auth-token")
    if (!token) {
      window.location.href = "/"
    }
  }, [])

  return <CRMDashboard />
}
