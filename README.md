# Bleach Cluster

Bleach Cluster 0.1.1 is a separate BMW iDrive 7 app based on Mario Cluster’s interface and live gauge renderer. Choose Hollow Mask or Hollow Ichigo in the Themes tab. The artwork has its own layer and the renderer supplies live values.

![Hollow Ichigo bench preview](hollow-ichigo-preview.webp)

![Hollow Mask design reference](hollow-mask-preview.webp)

In MGU Store, add or refresh `gladiator175/bleach-mgu-gauges` on `main`. The app requires `cluster-render` 0.5.1 or later. While parked, turn off any other custom cluster app before enabling Bleach Cluster. The Bleach toggle starts Off and uses the existing BMW vehicle pairing. Confirm factory indicators are visible and the Off toggle restores the factory display.

While stationary with the engine off in accessory or ignition mode, gauge updates run at 4 Hz. Live samples resume when the engine runs or the car moves. Rapid theme selections are combined into one redraw.

The store build was verified locally with an SDK stub. Installation and compositor behavior on the vehicle remain unverified.
