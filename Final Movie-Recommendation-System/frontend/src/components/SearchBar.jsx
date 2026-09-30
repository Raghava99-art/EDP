export default function SearchBar({ value, onChange, onSearch }) {
  return (
    <form
      className="search"
      onSubmit={event => {
        event.preventDefault();
        onSearch();
      }}
    >
      <input
        value={value}
        onChange={event => onChange(event.target.value)}
        placeholder="Search by title, genre, description..."
      />
      <button type="submit">Search</button>
    </form>
  );
}
