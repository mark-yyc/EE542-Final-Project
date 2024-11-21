package com.example.calorie_track.fragment;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.calorie_track.R;
import com.example.calorie_track.util.Constant;

public class GalleryFragment extends Fragment {
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_gallery, container, false);
        WebView webView = root.findViewById(R.id.webViewMap);
        webView.setWebViewClient(new WebViewClient()); // Prevent opening in external browser
        webView.getSettings().setJavaScriptEnabled(true); // Enable JavaScript if required

        // Load the map from your backend server
        String mapUrl = Constant.FLASK_BASE_URL+ "map"; // Replace <server_ip> with your server's IP address
        webView.loadUrl(mapUrl);
        return root;
    }
}