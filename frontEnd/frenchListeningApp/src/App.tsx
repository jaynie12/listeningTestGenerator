import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home.tsx";
// import Portal from "./pages/Portal";
// import PublicTests from "./pages/PublicTests";

function App() {
    return (
        <BrowserRouter>
            <div>
                <h1>Listening Test Generator</h1>
                <nav>
                    <Link to="/">Home</Link>
                </nav>
                <Routes>
                    <Route path="/" element={<Home />} />
                    {/* <Route path="/portal" element={<Portal />} /> */}
                    {/* <Route path="/public-tests" element={<PublicTests />} /> */}
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;
