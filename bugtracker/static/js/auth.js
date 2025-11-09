function parseJwt(token) {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    return JSON.parse(atob(base64));
}

function scheduleTokenRefresh() {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) return;

    const decoded = parseJwt(accessToken);
    const expiresAt = decoded.exp * 1000; // convert to ms
    const now = Date.now();

    const refreshIn = expiresAt - now - (30 * 1000); // refresh 30s before expiry

    if (refreshIn <= 0) {
        refreshAccessToken();
    } else {
        setTimeout(refreshAccessToken, refreshIn);
    }
}

async function refreshAccessToken() {
    const refreshToken = localStorage.getItem("refresh_token");
    if (!refreshToken) return;

    const response = await fetch("/auth/api/token/refresh/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh: refreshToken })
    });

    const data = await response.json();
    if (data.access) {
        localStorage.setItem("access_token", data.access);
        scheduleTokenRefresh(); // schedule next refresh
    } else {
        // refresh token dead → require login
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        window.location.href = "/auth/login/";
    }
}

// Start auto-refresh when page loads
document.addEventListener("DOMContentLoaded", scheduleTokenRefresh);
