import classes from "./MyInput.module.css";

export function MyInput(props) {
  return <input {...props} className={classes.myInput} />;
}