import { useState } from "react";
import axios from "axios";

const CreateUser = () => {
  const [nombre, setNombre] = useState("");
  const [apellido, setApellido] = useState("");
  const API_URL = "http://127.0.0.1:7500/users";

  const handleSubmit = async(e)=>{
    e.preventDefault();
    try{
      const response = await axios.post(API_URL, {
        nombre, // "nombre": valor
        apellido // "apellido": valor
      });
      if(response.status === 200){
        alert("Usuario creado con exito");
        setNombre("");
        setApellido("");
      }
    }catch(error){
      console.log(error)
    }
  }
  return <>
  
  <div>
    <form onSubmit={handleSubmit} action="">
      <div>
        <label htmlFor="">Nombre</label>
        <input type="text" name="nombre" id="nombre" onChange={(e)=> setNombre(e.target.value)} value={nombre} />
      </div>
      <div>
        <label htmlFor="">Apellido</label>
        <input type="text" name="apellido" id="apellido" onChange={(e)=> setApellido(e.target.value)} value={apellido} />
      </div>
      <button  type="submit">Registrar</button>
    </form>
  </div>
  </>;
};

export default CreateUser;
