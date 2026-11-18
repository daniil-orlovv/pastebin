import { useReducer, useRef, useState } from "react";
import "./styles/App.css";
import PostList from "./components/PostList";
import MyButton from "./components/UI/button/MyButton";
import { MyInput } from './components/UI/input/MyInput';
import PostForm from "./components/PostForm";
import MySelect from "./components/MySelect";

function App() {

  const [posts, setPosts] = useState(
    [
      {id: 1, title: 'JS1', body: 'JS'},
      {id: 2, title: 'JS2', body: 'JS'},
      {id: 3, title: 'JS3', body: 'JS'},
    ]
  )
  const [selectedSort, setSelectedSort] = useState('')

  function createPost(newPost) {
    setPosts([...posts, newPost ])
  }

  function removePost(post) {
    setPosts(posts.filter(p => p.id !== post.id))
  }

  function sortPosts(sort) {
    setSelectedSort(sort);
    console.log(sort)
    setPosts([...posts].sort((a, b) => a[sort].localeCompare(b[sort])))
  }

  return (
    <div className="App">
      <PostForm create={createPost} />
      <hr style={{margin: '15px 0px'}}></hr>
      <MySelect
        value={selectedSort}
        onChange={sortPosts}
        defaultValue='Сортировка по'
        options={
            [
            {value: 'title', name: 'названию'},
            {value: 'body', name: 'описанию'},
          ]
        }
      />
      {posts.length !== 0
        ? <PostList remove={removePost} posts={posts} title={'Посты'}/>
        : <h1 style={{textAlign: 'center'}}>Посты не найдены!</h1>
      }


      {/* <Counter/> */}
      {/* <Post post={{id: 1, title: 'Название', body: 'Тело'}}></Post> */}
    </div>
  );
}

export default App;
