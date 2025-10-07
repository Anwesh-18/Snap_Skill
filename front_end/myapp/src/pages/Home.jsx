import { Link } from "react-router-dom";
export default function HomePage() {
  return (
    <div className="h-screen w-screen bg-cover bg-center flex flex-col absolute inset-0" style={{ backgroundImage: "url('/backimg_2.jpg')" }}>
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
        {/* <h2 className="text-5xl text-blue-500 font-extrabold mb-4">SnapSkill</h2> */}
        <p className="text-xl max-w-xl mb-8">
          A platform where freelancers and companies connect through <span className="font-semibold">skills</span>, not resumes.
        </p>
        <div className="space-x-4">
          <a
          href="/freelancer" 
          className="bg-white text-blue-600 px-6 py-3 rounded-xl font-semibold shadow-lg hover:shadow-2xl transition">
            Join as Freelancer
          </a>
          <a
          href ="/company"
          className="bg-white text-black px-6 py-3 rounded-xl font-semibold shadow-lg hover:shadow-2xl transition">
            Join as Company
          </a>
        </div>
      </div>
      {/* Footer */}
      <footer className="text-center text-white py-4 text-sm">
        © {new Date().getFullYear()} SnapSkill. All rights reserved.
      </footer>
    </div>
  );
}