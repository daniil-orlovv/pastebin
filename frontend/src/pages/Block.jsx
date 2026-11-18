import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import classes from './Block.module.css'


function Block() {

  const { hash_url } = useParams();
  const [blockData, setBlockData] = useState(null);

  useEffect(() => {
    async function fetchBlock() {
      try {
        // Используем полученный hash_url в запросе к API или функции поиска
        const response = await fetch(`http://localhost:8000/api/blocks/get/${hash_url}/`, {
          method: 'POST', // Указываем нужный метод
          headers: {
            'Content-Type': 'application/json',
          }
          // body: JSON.stringify({ uuid: hash_url })
        });
        const data = await response.json();
        console.log(data)
        setBlockData(data);
      } catch (error) {
        console.error('Ошибка при получении блока:', error);
      }
    }

    if (hash_url) {
      fetchBlock();
    }
  }, [hash_url]); // Зависимость гарантирует повторный вызов, если ссылка изменится

  if (!blockData) return <div>Загрузка...</div>;


  return (
    <div>
      <div>
        <h1>Блок: {hash_url}</h1>
        <p style={{ whiteSpace: 'pre-wrap' }} className={classes.Block__p}>{blockData.block}</p>
      </div>
      <button>
        <Link to="/">Создать еще</Link>
      </button>
    </div>
  );
}

export default Block