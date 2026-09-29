import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [animes, setAnimes] = useState([])
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch('/api/animes/')
      .then((res) => {
        if (!res.ok) {
          throw new Error('Error al conectar con la API de Django')
        }
        return res.json()
      })
      .then((data) => {
        setAnimes(data.results || [])
        setCargando(false)
      })
      .catch((err) => {
        setError(err.message)
        setCargando(false)
      })
  }, [])

  return (
    <div>
      {cargando && <p>Cargando animes desde el servidor...</p>}

      {error && <p>Error: {error}</p>}

      {!cargando && !error && (
        <div>
          {animes.map((anime) => (
            <div key={anime.id}>
              <h2>{anime.titulo}</h2>
              <p>Episodios: {anime.episodios}</p>
              <p>
                Estado: {anime.visto ? '✅ Visto' : '⏳ Pendiente'}
              </p>
              <p>{anime.sinopsis}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default App