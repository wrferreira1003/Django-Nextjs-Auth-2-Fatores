import Image from "next/image";
import LoginForn from "../Login";
import { Box } from "@mui/material";

export default function Home() {
  return (
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      minHeight="100vh"
      flexDirection='column'
    >
    <LoginForn />
    </Box>
  );
}
