import Logo from './logo.png'
import { Link } from "react-router-dom";
import "./Picker.css";


export const Picker = () => {
  return (
    <>
    <div className="main-container">
      <div className="text">Această adresă nu mai este validă de la data de 25 ianuarie 2022. În cazul în care dorești să accesezi UMFQuiz, click mai jos. </div>
        <a href="https://umfquizwinter.github.io/UMF-Quiz-Winter/">
          <button className='subject-button'>Du-mă la <b>UMFQuiz</b></button>
        </a>
    </div>
    </>
  );
};

export default Picker;
