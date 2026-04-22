# Continue with About section
about_section = '''
    <!-- Terminal About Section -->
    <section id="about" class="py-20 relative">
        <div class="container mx-auto px-6">
            <div class="terminal-window bg-void-light/50 backdrop-blur-sm border border-neon/20 rounded-lg max-w-4xl mx-auto">
                <div class="terminal-header bg-void-light/80 px-4 py-2 flex items-center space-x-2 rounded-t-lg border-b border-neon/20">
                    <div class="w-3 h-3 rounded-full bg-red-500"></div>
                    <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                    <div class="w-3 h-3 rounded-full bg-green-500"></div>
                    <div class="text-sm text-gray-400 ml-4 font-cyber">bhavan@portfolio:~$</div>
                </div>
                <div class="p-8">
                    <div class="font-cyber text-neon mb-4">
                        <div class="mb-1">$ cat about.txt</div>
                    </div>
                    
                    <div class="text-gray-300 space-y-4 mb-8">
                        <h2 class="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-neon to-electric">
                            Decoding the engineer behind the innovation
                        </h2>
                        
                        <p>
                            I transform complex engineering concepts into elegant digital realities. With a background in 
                            Electronics & Communication Engineering and hands-on experience in software development, 
                            I bridge the gap between hardware understanding and creative software expression.
                        </p>
                        
                        <p>
                            My journey began with circuit designs and evolved through frontend development, machine learning, 
                            and now encompasses everything from AI-powered chatbots to computer vision applications that 
                            push the boundaries of what's possible.
                        </p>
                        
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-12">
                            <div class="text-center">
                                <div class="text-4xl font-bold text-neon font-cyber">95%</div>
                                <div class="text-sm text-gray-400">ML Model Accuracy</div>
                            </div>
                            <div class="text-center">
                                <div class="text-4xl font-bold text-electric font-cyber">8.81</div>
                                <div class="text-sm text-gray-400">Academic CGPA</div>
                            </div>
                            <div class="text-center">
                                <div class="text-4xl font-bold text-cyber font-cyber">3+</div>
                                <div class="text-sm text-gray-400">Major Projects</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section class="py-20 bg-void-light/30">
        <div class="container mx-auto px-6">
            <h2 class="text-4xl font-bold text-center mb-16 font-cyber neon-text">
                <span class="text-neon">$</span> cat education.log
            </h2>
            
            <div class="max-w-4xl mx-auto">
                <div class="hologram border border-neon/30 rounded-lg p-8 bg-void-light/20">
                    <div class="flex items-center justify-between mb-4">
                        <div>
                            <h3 class="text-2xl font-bold text-neon">Bachelor of Engineering</h3>
                            <p class="text-xl text-electric">Electronics & Communication Engineering</p>
                            <p class="text-gray-400">Panimalar Engineering College, Chennai</p>
                        </div>
                        <div class="text-right">
                            <div class="text-3xl font-bold text-cyber font-cyber">8.81</div>
                            <div class="text-sm text-gray-400">CGPA</div>
                            <div class="text-sm text-gray-400">2022 - 2026</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

print("Created about and education sections")
print("Length so far:", len(updated_html + body_content_updated + about_section))

# Continue with Skills section
skills_section = '''
    <!-- Skills Section -->
    <section id="skills" class="py-20 bg-void-light/30">
        <div class="container mx-auto px-6">
            <div class="terminal-window bg-void-light/50 backdrop-blur-sm border border-neon/20 rounded-lg max-w-6xl mx-auto">
                <div class="terminal-header bg-void-light/80 px-4 py-2 flex items-center space-x-2 rounded-t-lg border-b border-neon/20">
                    <div class="w-3 h-3 rounded-full bg-red-500"></div>
                    <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
                    <div class="w-3 h-3 rounded-full bg-green-500"></div>
                    <div class="text-sm text-gray-400 ml-4 font-cyber">bhavan@skills:~$</div>
                </div>
                <div class="p-8">
                    <div class="font-cyber text-neon mb-8">
                        <div class="mb-1">$ scan_skills --all</div>
                        <div class="text-gray-400">Scanning technological arsenal...</div>
                    </div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                        <!-- Programming Languages -->
                        <div class="skill-category">
                            <h3 class="text-xl font-bold text-electric mb-4">Languages</h3>
                            <div class="space-y-2">
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Python</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-14 h-2 bg-neon rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>JavaScript</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-13 h-2 bg-electric rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Java</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-12 h-2 bg-cyber rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>C/C++</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-11 h-2 bg-plasma rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>SQL</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-12 h-2 bg-neon rounded-full"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Frameworks -->
                        <div class="skill-category">
                            <h3 class="text-xl font-bold text-electric mb-4">Frameworks</h3>
                            <div class="space-y-2">
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>React JS</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-14 h-2 bg-electric rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Node JS</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-13 h-2 bg-neon rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Django</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-12 h-2 bg-cyber rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Express JS</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-11 h-2 bg-plasma rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>MongoDB</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-10 h-2 bg-electric rounded-full"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Tools -->
                        <div class="skill-category">
                            <h3 class="text-xl font-bold text-electric mb-4">Tools</h3>
                            <div class="space-y-2">
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Git</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-14 h-2 bg-neon rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Docker</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-12 h-2 bg-electric rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>AWS</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-11 h-2 bg-cyber rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>VS Code</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-15 h-2 bg-plasma rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>PyCharm</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-13 h-2 bg-neon rounded-full"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Libraries -->
                        <div class="skill-category">
                            <h3 class="text-xl font-bold text-electric mb-4">ML Libraries</h3>
                            <div class="space-y-2">
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Pandas</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-14 h-2 bg-neon rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>NumPy</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-13 h-2 bg-electric rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Scikit-learn</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-12 h-2 bg-cyber rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>OpenCV</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-13 h-2 bg-plasma rounded-full"></div>
                                    </div>
                                </div>
                                <div class="skill-item flex items-center justify-between p-2 rounded bg-void-light/30">
                                    <span>Matplotlib</span>
                                    <div class="w-16 h-2 bg-void-light rounded-full">
                                        <div class="w-11 h-2 bg-neon rounded-full"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

print("Created skills section")
print("Continuing with projects section...")

print("Total sections created so far")
print("Length:", len(updated_html + body_content_updated + about_section + skills_section))