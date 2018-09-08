
export function getConfig() {
    var tokenLatest = localStorage.getItem('token');
    return {
        headers: { 'Authorization': tokenLatest, 'Content-Type': 'application/json' }
    };
}