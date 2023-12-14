import axios from "axios"

export default(url = 'http://localhost:8000/api') => {
    return axios.create({
        baseURL: url,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        withCredentials: true})
}