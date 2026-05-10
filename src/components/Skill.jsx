import { skillsData } from "../assets.js";

const Skill = () => {
  return (
    <section id="skills" className="py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-14">
          <p className="text-sm uppercase tracking-[0.4em] text-teal-700 font-semibold mb-4">My skills</p>
          <h2 className="text-4xl sm:text-5xl font-bold mb-4">
            <span className="text-teal-600">Technical</span> Skills
          </h2>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            These are the tools and technologies I use when building web applications.
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {skillsData.map((skill) => (
            <div key={skill.title} className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">
              <h3 className="text-xl font-semibold text-slate-900 mb-4">{skill.title}</h3>
              <ul className="space-y-3 text-slate-600">
                {skill.items.map((item) => (
                  <li key={item} className="rounded-xl border border-slate-200 bg-slate-50 px-4 py-3">
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Skill;