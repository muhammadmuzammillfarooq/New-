import Portfolio1 from "../assets/Portfolio1.jpg";
import Portfolio2 from "../assets/Portfolio2.jpg";
import Portfolio3 from "../assets/Portfolio3.jpg";
import Portfolio4 from "../assets/Portfolio4.jpg";

const images = [
  { src: Portfolio1, alt: "Portfolio project 1", title: "React Landing Page", description: "A responsive landing page built with React and Tailwind CSS." },
  { src: Portfolio2, alt: "Portfolio project 2", title: "Dashboard UI", description: "A clean dashboard interface designed for productivity and analytics." },
  { src: Portfolio3, alt: "Portfolio project 3", title: "Portfolio Clone", description: "A modern portfolio website demonstrating layout and design skills." },
  { src: Portfolio4, alt: "Portfolio project 4", title: "Agency Website", description: "A polished marketing website with interactive sections and graphics." },
];

const Work = () => {
  return (
    <section id="work" className="py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="mb-16 text-center">
          <p className="text-sm uppercase tracking-widest text-teal-700 font-semibold mb-4">Featured work</p>
          <h2 className="text-4xl font-bold text-slate-900 mb-4">Projects I&rsquo;ve Built</h2>
          <p className="text-lg text-slate-600 max-w-3xl mx-auto">
            Web applications built with modern layout techniques, strong usability, and responsive design.
          </p>
        </div>

        <div className="grid gap-7 md:grid-cols-2 xl:grid-cols-4">
          {images.map((image, index) => (
            <div key={index} className="group overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm transition hover:-translate-y-1 hover:shadow-xl">
              <div className="overflow-hidden">
                <img src={image.src} alt={image.alt} className="h-56 w-full object-cover transition duration-500 group-hover:scale-105" />
              </div>
              <div className="p-6">
                <h3 className="text-lg font-semibold text-slate-900 mb-2">{image.title}</h3>
                <p className="text-sm leading-6 text-slate-600">{image.description}</p>
                <div className="mt-6 flex flex-wrap gap-3">
                  <a href="#" className="inline-flex rounded-full bg-teal-600 px-4 py-2 text-sm font-semibold text-white transition hover:bg-teal-500">Live Demo</a>
                  <a href="#" className="inline-flex rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-semibold text-slate-700 transition hover:border-teal-500 hover:text-teal-500">Source</a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Work;