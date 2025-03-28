#include <gtkmm.h>
#include <gst/gst.h>
#include <fstream>
#include <vector>
#include <sstream>

struct Channel {
    std::string name;
    std::string url;
};

class Catch! : public Gtk::Window {
public:
    Catch!();
    virtual ~Catch!();

private:
    void on_channel_selected();
    void on_play_clicked();
    void setup_gstreamer();
    void load_m3u_playlist(const std::string& filename);

    Gtk::Box m_main_box, m_side_box;
    Gtk::Button m_play_button;
    Gtk::ScrolledWindow m_channel_scroll;
    Gtk::TreeView m_channel_list;
    Glib::RefPtr<Gtk::ListStore> m_list_store;
    
    Glib::RefPtr<Gst::Element> m_pipeline;

    struct ModelColumns : public Gtk::TreeModel::ColumnRecord {
        ModelColumns() { add(name); add(url); }
        Gtk::TreeModelColumn<std::string> name;
        Gtk::TreeModelColumn<std::string> url;
    } m_columns;

    std::vector<Channel> m_channels;
};

Catch!::Catch!() 
    : m_main_box(Gtk::Orientation::HORIZONTAL), 
      m_side_box(Gtk::Orientation::VERTICAL), 
      m_play_button("Play") {

    set_title("Catch!");
    set_default_size(900, 500);

    set_child(m_main_box);
    
    m_list_store = Gtk::ListStore::create(m_columns);
    m_channel_list.set_model(m_list_store);
    m_channel_list.append_column("Channel", m_columns.name);

    m_channel_scroll.set_child(m_channel_list);
    m_channel_scroll.set_policy(Gtk::PolicyType::AUTOMATIC, Gtk::PolicyType::AUTOMATIC);
    m_side_box.append(m_channel_scroll);
    m_side_box.append(m_play_button);
    m_main_box.append(m_side_box);

    m_play_button.signal_clicked().connect(sigc::mem_fun(*this, &Catch!::on_play_clicked));
    m_channel_list.signal_row_activated().connect(sigc::mem_fun(*this, &Catch!::on_channel_selected));

    setup_gstreamer();

    load_m3u_playlist("channels.m3u");
}

Catch!::~Catch!() {
    if (m_pipeline) {
        gst_element_set_state(m_pipeline->gobj(), GST_STATE_NULL);
    }
}

void Catch!::setup_gstreamer() {
    gst_init(nullptr, nullptr);
    m_pipeline = Gst::ElementFactory::create_element("playbin");
}

void Catch!::on_play_clicked() {
    if (!m_channels.empty() && m_pipeline) {
        gst_element_set_state(m_pipeline->gobj(), GST_STATE_PLAYING);
    }
}

void Catch!::on_channel_selected() {
    auto selected = m_channel_list.get_selection()->get_selected();
    if (selected) {
        std::string stream_url = (*selected)[m_columns.url];
        m_pipeline->set_property("uri", stream_url);
        gst_element_set_state(m_pipeline->gobj(), GST_STATE_PLAYING);
    }
}

void Catch!::load_m3u_playlist(const std::string& filename) {
    std::ifstream file(filename);
    if (!file) return;

    std::string line, name, url;
    while (std::getline(file, line)) {
        if (line.rfind("#EXTINF:", 0) == 0) {
            name = line.substr(line.find(",") + 1);
        } else if (line.rfind("http", 0) == 0) {
            url = line;
            m_channels.push_back({name, url});

            auto row = *(m_list_store->append());
            row[m_columns.name] = name;
            row[m_columns.url] = url;
        }
    }
}

int main(int argc, char* argv[]) {
    auto app = Gtk::Application::create("com.example.catch");
    Catch! player;
    return app->run(player);
}
