import axios from "axios";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
const EditUser = () => {
  const { id } = useParams();
  const [user, setUser] = useState({
    nombre: "",
    apellido: "",
  });

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:7500/users/${id}`);
        if (response.status === 200) {
          setUser(response.data);
        }
      } catch (error) {
        console.log(error);
      }
    };
    fetchUser();
  }, [id]);

  const handleInputChange = (e) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.patch(`http://127.0.0.1:7500/users/${id}`, user); // {"nombre":"valor", "apellido":"valor"}
      alert("Usuario actualizado con exito");
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      <div>
        <form action="" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="">Nombre</label>
            <input
              type="text"
              name="nombre"
              id="nombre"
              onChange={handleInputChange}
              value={user.nombre}
            />
          </div>
          <div>
            <label htmlFor="">Apellido</label>
            <input
              type="text"
              name="apellido"
              id="apellido"
              onChange={handleInputChange}
              value={user.apellido}
            />
          </div>
          <button type="submit">Guardar cambios</button>
        </form>
      </div>
    </>
  );
};

export default EditUser;
