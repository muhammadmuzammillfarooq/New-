import Navbar from "../components/Navbar.jsx";
import Hero from "../components/Hero.jsx";
import About from "../components/About.jsx";
import Work from "../components/Work.jsx";
import Skill from "../components/Skill.jsx";
import Contact from "../components/Contact.jsx";

const Home = () => {
  return (
    <div className="bg-slate-50 text-slate-900">
      <Navbar />
      <Hero />
      <About />
      <Work />
      <Skill />
      <Contact />
    </div>
  );
};

export default Home;