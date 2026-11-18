import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import classes from './Block.module.css';


function Block() {

  const { hash_id } = useParams();
  const navigate = useNavigate();
  const [blockData, setBlockData] = useState(null);

  useEffect(() => {
    async function fetchBlock() {
      try {
        // Используем полученный hash_url в запросе к API или функции поиска
        const response = await fetch(`http://localhost:8000/api/blocks/get/${hash_id}/`, {
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

    if (hash_id) {
      fetchBlock();
    }
  }, [hash_id]); // Зависимость гарантирует повторный вызов, если ссылка изменится

  if (!blockData) return <div>Загрузка...</div>;


  return (
    <div>
      <div>
        <h1>Блок: {hash_id}</h1>
        <p style={{ whiteSpace: 'pre-wrap' }} className={classes.Block__p}>{blockData.text}</p>
      </div>
      <div className={classes.Block__under}>
        <button onClick={() => navigate('/')}>Создать еще</button>
        <p className={classes.Block__views}>
          Просмотры: {blockData.views}
        </p>
        <p>
          Дата и время удаления: {blockData.ttl}
        </p>
      </div>

    </div>
  );
}

export default Block