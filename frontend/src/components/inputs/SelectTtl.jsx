import classes from './SelectTtl.module.css'

const SelectTtl = ( { dateTtl, setDateTtl, timeTtl, setTimeTtl }) => {
  return (
    <div>
        <div>
            <p className={classes.SelectTtl__p}>
                Дата и время удаления
            </p>
        </div>
        <div className={classes.SelectTtl__datetime}>
            <input
            type="date"
            value={dateTtl}
            onChange={e => setDateTtl(e.target.value)}
            min="2026-01-01"
            max="2026-12-31"
            >
            </input>
            <input
                type="time"
                value={timeTtl}
                onChange={e => setTimeTtl(e.target.value)}
                min="00:00"
                max="23:59"
            >
            </input>
        </div>

    </div>
  )
}

export default SelectTtl