import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <img src="{{ url_for('video') }}" width="50%"/>
    </div>
  );
}

export default App;
