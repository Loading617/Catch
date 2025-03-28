#include <gtkmm.h>
#include <gst/gst.h>

class Catch! : public Gtk::Window {
public:
    IPTVPlayer();
    virtual ~Catch!();

private:
    void on_play_clicked();
    void setup_gstreamer();
    
    Gtk::Box m_main_box;
    Gtk::Button m_play_button;
    Glib::RefPtr<Gst::Element> m_pipeline;
};

Catch!::Catch!() 
    : m_main_box(Gtk::Orientation::VERTICAL), 
      m_play_button("Play") {
    
    set_title("Catch!");
    set_default_size(863, 520);

    m_main_box.append(m_play_button);
    set_child(m_main_box);
    
    m_play_button.signal_clicked().connect(sigc::mem_fun(*this, &Catch!::on_play_clicked));
    
    setup_gstreamer();
}

Catch!::~Catch!() {
    if (m_pipeline) {
        gst_element_set_state(m_pipeline->gobj(), GST_STATE_NULL);
    }
}

void Catch!::setup_gstreamer() {
    gst_init(nullptr, nullptr);
    m_pipeline = Gst::ElementFactory::create_element("playbin");
    
    if (!m_pipeline) {
        g_printerr("Failed to create playbin\n");
        return;
    }

    m_pipeline->set_property("uri", "http://example.com/stream.m3u8");
}

void Catch!::on_play_clicked() {
    if (m_pipeline) {
        gst_element_set_state(m_pipeline->gobj(), GST_STATE_PLAYING);
    }
}

int main(int argc, char* argv[]) {
    auto app = Gtk::Application::create("com.example.catch!");
    Catch! player;
    return app->run(player);
}
