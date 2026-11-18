import React from 'react'
import classes from './Editor.module.css'
import MyButton from '../buttons/Button'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import SelectTtl from './SelectTtl';

const Editor = ({blocks, block, setBlocks, setBlock}) => {

  const [loading, setLoading] = useState(false);
  const [dateTtl, setDateTtl] = useState('')
  const [timeTtl, setTimeTtl] = useState('')
  const navigate = useNavigate();

  function formatTtl(dateStr, timeStr = '00:00') {
    const [year, month, day] = dateStr.split('-');
    return `${day}-${month}-${year} ${timeStr}`;
  }

  const dateTimeTtl = formatTtl(dateTtl, timeTtl)

  const submit = async (event) => {
    event.preventDefault();

    setLoading(true);
    const response = await fetch('http://localhost:8000/api/blocks/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: block,
        ttl: dateTimeTtl
      }),
    });
    const result = await response.json()
    console.log(result)
    console.log('Блок создался на бэке');
    navigate('/created', {
      state: { hash_id: result.hash_id, views: result.views },
    });

    setBlock('');

    setLoading(false);
  };

  return (
    <form className={classes.form} onSubmit={submit}>
        <textarea
          value={block}
          onChange={e => setBlock(e.target.value)}
          className={classes.textarea}
          placeholder='Введите текст'
        />
        <div className={classes.form_inputs}>
          <MyButton
            type='submit'
            disabled={loading}
          >
            {loading ? 'Создаём...' : 'Создать'}
          </MyButton>
          <SelectTtl
            dateTtl={dateTtl}
            setDateTtl={setDateTtl}
            timeTtl={timeTtl}
            setTimeTtl={setTimeTtl}
          >

          </SelectTtl>
        </div>
    </form>
  )
}

export default Editor