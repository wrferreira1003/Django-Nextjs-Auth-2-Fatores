'use client'

import { Button, TextField } from "@mui/material";
import { useState } from "react";

export default function LoginForn() {
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

    }

    return (
        <form onSubmit={handleLogin}>
      <TextField
        label="Usuário"
        variant="outlined"
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
        required
      />
      <TextField
        label="Senha"
        type="password"
        variant="outlined"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <Button type="submit" variant="contained" color="primary">
        Entrar
      </Button>
    </form>
    )

}