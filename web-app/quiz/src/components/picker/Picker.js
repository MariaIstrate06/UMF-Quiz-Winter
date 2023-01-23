import Logo from './logo.png'
import { Link } from "react-router-dom";
import "./Picker.css";


export const Picker = () => {
  return (
    <>
    <div className="page-container">
        <div className="image-container">
        <img src={Logo} style={{width: "60%", maxWidth: "300px"}}></img> 
        </div>
        <div className="page">
        <button className="subject-button">
            <Link to="/UMF-Quiz-Winter/card/anato">
            Anatomie
            </Link>
        </button>
        <button className="subject-button">
            <Link to="/UMF-Quiz-Winter/card/diabet">
            Diabet
            </Link>
        </button>
        </div>
    </div>
    </>
  );
};

export default Picker;
