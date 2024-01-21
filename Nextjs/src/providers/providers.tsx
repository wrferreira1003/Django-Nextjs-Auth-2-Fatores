'use client'
import { ThemeProvider } from "@emotion/react";
import theme from "../Themes/theme";
import { CssBaseline } from "@mui/material";


export default function Provider( { children }: { children: React.ReactNode }) {
    return (
        <>
        <ThemeProvider theme={theme}>
        <CssBaseline />    
        {children}
        </ThemeProvider>s
        </>
    );
}