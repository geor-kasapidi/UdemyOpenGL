#version 330 core

struct Light {
    vec3 position;
    vec3 color;
};

#define NUM_LIGHTS 1

uniform Light light_data[NUM_LIGHTS];

uniform sampler2D tex;

in vec3 color;
in vec3 normal;
in vec3 frag_pos;
in vec3 view_pos;
in vec2 UV;

out vec4 frag_color;

vec4 createLight(vec3 light_pos, vec3 light_color, vec3 normal, vec3 frag_pos, vec3 view_dir) {
    //ambient
    float a_strength = 0.1;
    vec3 ambient = a_strength * light_color;
    
    //diffuse
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - frag_pos);
    float diff = max(dot(norm, light_dir), 0);
    vec3 diffuse = diff * light_color;
    
    //specular
    float s_strength = 0.3;
    vec3 reflect_dir = normalize(-light_dir - norm);
    float spec = pow(max(dot(view_dir, reflect_dir), 0), 32);
    vec3 specular = s_strength * spec * light_color;
    
    return vec4(color * (ambient + diffuse + specular), 1);
}

void main() {
    vec3 view_dir = normalize(view_pos - frag_pos);
    frag_color = vec4(0,0,0,1);
    for(int i=0; i<NUM_LIGHTS; i++) {
        frag_color += createLight(light_data[i].position, light_data[i].color, normal, frag_pos, view_dir);
    }
    frag_color *= texture(tex, UV);
}
