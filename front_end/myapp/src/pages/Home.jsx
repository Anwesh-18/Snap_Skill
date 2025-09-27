import { Link } from "react-router-dom";
export default function HomePage() {
  return (
    <div className="bg-gradient-to-r from-blue-500 to-purple-600 min-h-screen flex flex-col">
      {/* Navbar */}
      <nav className="flex justify-between items-center px-8 py-4 text-white">
        <h1 className="text-2xl font-bold">SnapSkill</h1>
        <div className="space-x-6">
          <a href="#" className="hover:underline">About</a>
          <a href="#" className="hover:underline">Features</a>
          <a href="#" className="hover:underline">Contact</a>
          <a href="#" className="hover:underline">Login</a>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="flex flex-col items-center justify-center flex-grow text-center text-white px-6">
        <h2 className="text-5xl font-extrabold mb-4">SnapSkill</h2>
        <p className="text-xl max-w-xl mb-8">
          A platform where freelancers and companies connect through <span className="font-semibold">skills</span>, not resumes.
        </p>

        <div className="space-x-4">
          <Link
          to={"/freelancer"} 
          className="bg-white text-blue-600 px-6 py-3 rounded-xl font-semibold shadow-lg hover:shadow-2xl transition">
            Join as Freelancer
          </Link>
          <Link 
          to={"/company"}
          className="bg-yellow-400 text-black px-6 py-3 rounded-xl font-semibold shadow-lg hover:shadow-2xl transition">
            Join as Company
          </Link>
        </div>
      </div>

      {/* Footer */}
      <footer className="text-center text-white py-4 text-sm">
        © {new Date().getFullYear()} SnapSkill. All rights reserved.
      </footer>
    </div>
  );
}