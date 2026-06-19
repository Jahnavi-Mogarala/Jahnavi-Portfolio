import re

cert_html = """  <div class="projects">
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">CRUD Operations in MongoDB</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">MongoDB Overview</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">AI Tools Workshop</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Applying AI Principles with Google Cloud</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Participation in Qualified Dilemma (Shaastra, IIT Madras)</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Introduction to IoT and Digital Transformation</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Getting Started with Artificial Intelligence</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">AWS Cloud Practitioner Certification - Self Paced</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Deloitte Australia - Technology Job Simulation</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Introduction to Generative AI</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Get started building apps for Microsoft Teams</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">SIH 2025 Certificate of Participation SRMIST</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">AI Literacy</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Certificate of Completion | Microsoft Interview Preparation</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
    <div class="cert-card">
      <h4><i class="fas fa-certificate"></i> <span class="parallelogram-darkblue" style="text-align:center; display:block;">Code Generation and Optimization Using IBM Granite</span></h4>
      <div class="links" style="text-align:center;">
        <a href="https://www.linkedin.com/in/mogarala-jahnavi-511b77257/details/certifications/" target="_blank"><p class="parallelogram-darkblue">View</p></a>
      </div>
    </div>
  </div>"""

with open(r'c:\Users\mogar\OneDrive\Documents\janu portfolio\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the content between <section class="Certifications-section" id="certifications"> and </section>
pattern = r'(<section class="Certifications-section" id="certifications">\s*<h2 class="section-title">Certifications</h2>\s*)<div class="projects">.*?</div>(\s*</section>)'
new_content = re.sub(pattern, r'\1' + cert_html + r'\2', content, flags=re.DOTALL)

with open(r'c:\Users\mogar\OneDrive\Documents\janu portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Certifications updated successfully.")
