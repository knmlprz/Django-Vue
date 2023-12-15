import api from "./api"

export const login = (email: string, password: string) => {
    api().post('/auth/login', {"email": email, "password": password})
}

export const logout = () => {
    api().post('/auth/logout')
}

export const getUser = () => {
    api().get('/auth/user')
}

export const register = (email: string, password: string, password_confirm: string) => {
    api().post('/auth/register', {'email': email, 'password': password, 'password_confirm': password_confirm})
}