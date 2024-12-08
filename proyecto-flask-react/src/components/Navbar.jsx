import { Link } from "react-router-dom";
const Navbar = () => {
  return (
    <>
      <nav className="h-[60px] flex justify-between items-center px-10 bg-slate-800">
        <p className="font-bold text-white text-2xl">Flask</p>
        <ul className="flex gap-5 justify-center items-center text-white font-bold">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/create-user">Crear usuario</Link>
          </li>
        </ul>
      </nav>
    </>
  );
};

export default Navbar;
