# Changelog

## 6.2.0 (2025-06-16)

Full Changelog: [v6.1.0...v6.2.0](https://github.com/revenium/revenium-metering-python/compare/v6.1.0...v6.2.0)

### Features

* **api:** api update ([ccd92ec](https://github.com/revenium/revenium-metering-python/commit/ccd92ecb8ecbfa09f68e84858be192ae54e47caa))
* **api:** api update ([679a7dd](https://github.com/revenium/revenium-metering-python/commit/679a7ddaf26b2bbdf1382adaab22c5fb65e54321))
* **api:** api update ([0ca6278](https://github.com/revenium/revenium-metering-python/commit/0ca62788ad0c28f677f7eb81cf15778e7b350f15))
* **api:** api update ([f73648f](https://github.com/revenium/revenium-metering-python/commit/f73648ff3165df6648416e1ffb0e1ac5b169a007))
* **api:** api update ([415d0f5](https://github.com/revenium/revenium-metering-python/commit/415d0f59bb4ae35bded8c49dae9f99af2684eb1d))
* **api:** api update ([4318a88](https://github.com/revenium/revenium-metering-python/commit/4318a88696d2e7603e768aef7e92249d59df7396))
* **api:** api update ([2746159](https://github.com/revenium/revenium-metering-python/commit/27461592779f0ea04bb903ac48709484f03f9985))
* **api:** api update ([74e914f](https://github.com/revenium/revenium-metering-python/commit/74e914fd5a8221613079602367ebf190ab93f20e))
* **api:** manual updates ([78b3242](https://github.com/revenium/revenium-metering-python/commit/78b32427d9c31580b44e7c4470344173dd796672))
* **client:** add follow_redirects request option ([b9173f8](https://github.com/revenium/revenium-metering-python/commit/b9173f8e4581a12f289d983464752d2890aab75b))


### Bug Fixes

* **client:** correctly parse binary response | stream ([581a1f2](https://github.com/revenium/revenium-metering-python/commit/581a1f297f81d32c2a144a8e11abc1a3130941a7))
* **package:** support direct resource imports ([1516201](https://github.com/revenium/revenium-metering-python/commit/151620100242547bab9a4f83b7dde38f61e1b2a1))


### Chores

* **ci:** fix installation instructions ([95fe222](https://github.com/revenium/revenium-metering-python/commit/95fe222d860373e69e1a33279fca563736c00dd9))
* **ci:** upload sdks to package manager ([b36eb61](https://github.com/revenium/revenium-metering-python/commit/b36eb61301c78ad50fc8d9a87256ad258973a660))
* **docs:** grammar improvements ([d3fbc0c](https://github.com/revenium/revenium-metering-python/commit/d3fbc0ca3e3107a08b0794c7f75158ddfccda31d))
* **docs:** remove reference to rye shell ([8484b83](https://github.com/revenium/revenium-metering-python/commit/8484b834101044653331d7b741b8ce5fb677b516))
* **internal:** avoid errors for isinstance checks on proxies ([a7f8d91](https://github.com/revenium/revenium-metering-python/commit/a7f8d912acb1503d1377a90c2f5a29c6c3eb6254))
* **tests:** run tests in parallel ([8963600](https://github.com/revenium/revenium-metering-python/commit/89636002231c7ebf82ff53fc933ed9a21ba58a44))

## 6.1.0 (2025-05-04)

Full Changelog: [v6.0.0...v6.1.0](https://github.com/revenium/revenium-metering-python/compare/v6.0.0...v6.1.0)

### Features

* **api:** api update ([42e362a](https://github.com/revenium/revenium-metering-python/commit/42e362a447ed75ea4180adb8af0bbdc119b5eefc))
* **api:** api update ([f0b08a2](https://github.com/revenium/revenium-metering-python/commit/f0b08a26bfc4a18c4b66ec430679ca90063fd96a))
* **api:** api update ([9b23ae6](https://github.com/revenium/revenium-metering-python/commit/9b23ae6e6e5bf231f9dcc5ff617114996d4ee841))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([79ff707](https://github.com/revenium/revenium-metering-python/commit/79ff707f1756d376d5b34ca3185b36bd40f949b5))


### Chores

* broadly detect json family of content-type headers ([9e221c3](https://github.com/revenium/revenium-metering-python/commit/9e221c33d5a74b7c2d503a5609c0310cfb5808a7))
* **ci:** add timeout thresholds for CI jobs ([0dc29df](https://github.com/revenium/revenium-metering-python/commit/0dc29dfd5d81a7c775d7b7740dd2dbd8266a80ab))
* **ci:** only use depot for staging repos ([bca62a0](https://github.com/revenium/revenium-metering-python/commit/bca62a02424aa66cbdaa60cce1c44afea85071b3))
* **internal:** codegen related update ([d529a06](https://github.com/revenium/revenium-metering-python/commit/d529a06e9c18e5c8029cb25b95e7bc5c5131873d))
* **internal:** fix list file params ([21c6f0d](https://github.com/revenium/revenium-metering-python/commit/21c6f0da9de70ecd48bf19e9eac8da8a3ad6636e))
* **internal:** import reformatting ([736cb66](https://github.com/revenium/revenium-metering-python/commit/736cb66a6e10d34c1d89928c8c5fd7a4e180099f))
* **internal:** refactor retries to not use recursion ([7e47381](https://github.com/revenium/revenium-metering-python/commit/7e473812e55d8c97691fa572ff5419310cbb8b5c))
* **internal:** update models test ([0bfe876](https://github.com/revenium/revenium-metering-python/commit/0bfe876d91020314ac3d3caa89b094adaf5c09de))

## 6.0.0 (2025-04-18)

Full Changelog: [v5.0.1...v6.0.0](https://github.com/revenium/revenium-metering-python/compare/v5.0.1...v6.0.0)

### Features

* **api:** manual updates ([2e9ea17](https://github.com/revenium/revenium-metering-python/commit/2e9ea17bf6fceb128d327b4059bdcb313f8ad1b0))

## 5.0.1 (2025-04-18)

Full Changelog: [v5.0.0...v5.0.1](https://github.com/revenium/revenium-metering-python/compare/v5.0.0...v5.0.1)

### Bug Fixes

* **perf:** optimize some hot paths ([23527ad](https://github.com/revenium/revenium-metering-python/commit/23527adaf33fe9d0532be78877f84327e9f3d825))
* **perf:** skip traversing types for NotGiven values ([969c1b2](https://github.com/revenium/revenium-metering-python/commit/969c1b2b7460274a81da3c41edf75b18d816cb5d))


### Chores

* **client:** minor internal fixes ([62996ae](https://github.com/revenium/revenium-metering-python/commit/62996aede8eb0e902edc2f1c7e9678f8718c4595))
* **internal:** base client updates ([13c7403](https://github.com/revenium/revenium-metering-python/commit/13c7403de2a87e8e1fa38d22ebca34ec55256d90))
* **internal:** bump pyright version ([c243d88](https://github.com/revenium/revenium-metering-python/commit/c243d88b0621031dcfcac106e7fa73eac38f7355))
* **internal:** update pyright settings ([20ffafd](https://github.com/revenium/revenium-metering-python/commit/20ffafda0131bf6cf849044c8e929691f59a36d6))

## 5.0.0 (2025-04-10)

Full Changelog: [v4.0.0...v5.0.0](https://github.com/revenium/revenium-metering-python/compare/v4.0.0...v5.0.0)

### Features

* **api:** api update ([da1e5a8](https://github.com/revenium/revenium-metering-python/commit/da1e5a8121ef399f31f20284168f37a7fc5d7a54))
* **api:** api update ([9cc4756](https://github.com/revenium/revenium-metering-python/commit/9cc47568f745453fdff63863ebfd69b2d3579895))
* **api:** api update ([02e77f5](https://github.com/revenium/revenium-metering-python/commit/02e77f57d2544ede9d0c3eb40e01744a685b3119))
* **api:** api update ([b6c84d9](https://github.com/revenium/revenium-metering-python/commit/b6c84d91b2b647d449129df6ce22c7ba94f5e0c1))
* **api:** api update ([edb7ea8](https://github.com/revenium/revenium-metering-python/commit/edb7ea8cad54dc36611d9b1d9d29e624c5d3cf2d))
* **api:** api update ([#21](https://github.com/revenium/revenium-metering-python/issues/21)) ([206dd6c](https://github.com/revenium/revenium-metering-python/commit/206dd6c2b49088eea94614750fd97c067db70b76))
* **api:** api update ([#25](https://github.com/revenium/revenium-metering-python/issues/25)) ([77334f1](https://github.com/revenium/revenium-metering-python/commit/77334f1f77b0f6ce3df41442f2037bb37e8d3dbf))
* **api:** api update ([#28](https://github.com/revenium/revenium-metering-python/issues/28)) ([af3f4f4](https://github.com/revenium/revenium-metering-python/commit/af3f4f43d57b478323acdc8d590cbbfa7ab8deda))
* **api:** api update ([#30](https://github.com/revenium/revenium-metering-python/issues/30)) ([56602fe](https://github.com/revenium/revenium-metering-python/commit/56602feec4cb371b126d89b7a3b7bcb173b8bfe8))
* **api:** api update ([#31](https://github.com/revenium/revenium-metering-python/issues/31)) ([b042007](https://github.com/revenium/revenium-metering-python/commit/b042007eca5954e9eaea93eeec9120a9f4f0e6e7))
* **api:** api update ([#32](https://github.com/revenium/revenium-metering-python/issues/32)) ([fec56ca](https://github.com/revenium/revenium-metering-python/commit/fec56ca89ce68cf98ee88c7f4fa283f9ed708b9c))
* **api:** api update ([#34](https://github.com/revenium/revenium-metering-python/issues/34)) ([d532f96](https://github.com/revenium/revenium-metering-python/commit/d532f9606c202832668d360d8a1fc7fe0d9e155a))
* **api:** api update ([#36](https://github.com/revenium/revenium-metering-python/issues/36)) ([c103db2](https://github.com/revenium/revenium-metering-python/commit/c103db2857567438cfc1154388134e6a3abf0f57))
* **api:** api update ([#41](https://github.com/revenium/revenium-metering-python/issues/41)) ([9ed8e89](https://github.com/revenium/revenium-metering-python/commit/9ed8e892ddd1f46bea22fe2df02aaccf881f96b9))
* **api:** api update ([#43](https://github.com/revenium/revenium-metering-python/issues/43)) ([4253f04](https://github.com/revenium/revenium-metering-python/commit/4253f04928d9d188e819911a203b852863d99970))
* **api:** api update ([#44](https://github.com/revenium/revenium-metering-python/issues/44)) ([3b3989a](https://github.com/revenium/revenium-metering-python/commit/3b3989a9b9a5deb03945241dd773d20466219265))
* **api:** api update ([#45](https://github.com/revenium/revenium-metering-python/issues/45)) ([e0edf27](https://github.com/revenium/revenium-metering-python/commit/e0edf27d7fb7eaa274a60b1cb90c06ec19384b23))
* **api:** api update ([#47](https://github.com/revenium/revenium-metering-python/issues/47)) ([fbaf56d](https://github.com/revenium/revenium-metering-python/commit/fbaf56d8b5a17b1ae394ea153190b1e9e2aaadcf))
* **api:** api update ([#50](https://github.com/revenium/revenium-metering-python/issues/50)) ([a341880](https://github.com/revenium/revenium-metering-python/commit/a34188079797aabad5ca3a8bffcc5105d4fa20c9))
* **api:** api update ([#52](https://github.com/revenium/revenium-metering-python/issues/52)) ([588453e](https://github.com/revenium/revenium-metering-python/commit/588453e52c8b990e1d49dd8ff3254176269f6cd3))
* **api:** api update ([#53](https://github.com/revenium/revenium-metering-python/issues/53)) ([35a5649](https://github.com/revenium/revenium-metering-python/commit/35a56490fe0b5fcc056a64de4d2a4ddc53bfea38))
* **api:** api update ([#54](https://github.com/revenium/revenium-metering-python/issues/54)) ([eca927e](https://github.com/revenium/revenium-metering-python/commit/eca927e776f763abe944064874c7ca0a0decd244))
* **api:** api update ([#56](https://github.com/revenium/revenium-metering-python/issues/56)) ([5c06d9e](https://github.com/revenium/revenium-metering-python/commit/5c06d9e608c0a1843585b97151780e1f6a96d9a7))
* **api:** api update ([#59](https://github.com/revenium/revenium-metering-python/issues/59)) ([7861dc4](https://github.com/revenium/revenium-metering-python/commit/7861dc4dde3675b297c37aed7b9e67c883857dfe))
* **api:** api update ([#62](https://github.com/revenium/revenium-metering-python/issues/62)) ([c790527](https://github.com/revenium/revenium-metering-python/commit/c79052789cd70eaee8171c09d0cfedb5a2e3bda5))
* **api:** api update ([#65](https://github.com/revenium/revenium-metering-python/issues/65)) ([4940606](https://github.com/revenium/revenium-metering-python/commit/494060672f8339627f2594d983f3289581754c12))
* **api:** api update ([#67](https://github.com/revenium/revenium-metering-python/issues/67)) ([56f305e](https://github.com/revenium/revenium-metering-python/commit/56f305eed29a2344e33664b676d12352902be00d))
* **api:** api update ([#70](https://github.com/revenium/revenium-metering-python/issues/70)) ([f3ef651](https://github.com/revenium/revenium-metering-python/commit/f3ef6510eb17cfd51beee437bb8b13a337dfbd2b))
* **api:** api update ([#72](https://github.com/revenium/revenium-metering-python/issues/72)) ([4211732](https://github.com/revenium/revenium-metering-python/commit/42117321009bd3eacdf80e51a5bb0f8ad59686f5))
* **api:** api update ([#73](https://github.com/revenium/revenium-metering-python/issues/73)) ([37572c1](https://github.com/revenium/revenium-metering-python/commit/37572c1d62635929861fffe62834f4cc87a3bd22))
* **api:** api update ([#74](https://github.com/revenium/revenium-metering-python/issues/74)) ([70ae4ff](https://github.com/revenium/revenium-metering-python/commit/70ae4ffff64bbc9be29ecb81afcbd4d96bc41e90))
* **api:** api update ([#75](https://github.com/revenium/revenium-metering-python/issues/75)) ([cc83c06](https://github.com/revenium/revenium-metering-python/commit/cc83c06a0e8b26a342f2df4940db98c16551a7e1))
* **api:** update via SDK Studio ([#16](https://github.com/revenium/revenium-metering-python/issues/16)) ([fda738b](https://github.com/revenium/revenium-metering-python/commit/fda738b99aa121b04df02a64987f8d003ef8055e))
* **api:** update via SDK Studio ([#8](https://github.com/revenium/revenium-metering-python/issues/8)) ([f68c95f](https://github.com/revenium/revenium-metering-python/commit/f68c95fed3c81e362a017a16677ea7b1af9b4aea))


### Bug Fixes

* **ci:** ensure pip is always available ([#18](https://github.com/revenium/revenium-metering-python/issues/18)) ([c92a6a3](https://github.com/revenium/revenium-metering-python/commit/c92a6a3430a507462b2d70a37dcc4525407faacb))
* **ci:** remove publishing patch ([#22](https://github.com/revenium/revenium-metering-python/issues/22)) ([a11a87b](https://github.com/revenium/revenium-metering-python/commit/a11a87b12a6e95e294e22d9037fafd93113b0961))
* **types:** handle more discriminated union shapes ([#15](https://github.com/revenium/revenium-metering-python/issues/15)) ([63317f4](https://github.com/revenium/revenium-metering-python/commit/63317f448fbe4590a19d82ba5c67da7be0a6c4ab))


### Chores

* fix typos ([#38](https://github.com/revenium/revenium-metering-python/issues/38)) ([719f112](https://github.com/revenium/revenium-metering-python/commit/719f11225e758eea6a1ae25b404040e4a853184b))
* go live ([#1](https://github.com/revenium/revenium-metering-python/issues/1)) ([65fd84b](https://github.com/revenium/revenium-metering-python/commit/65fd84ba27271c5e68054e8f4e5290e3e6cb339f))
* **internal:** bump rye to 0.44.0 ([#14](https://github.com/revenium/revenium-metering-python/issues/14)) ([614dbd4](https://github.com/revenium/revenium-metering-python/commit/614dbd4639c6ea18b16f91517bf91699562d5777))
* **internal:** codegen related update ([#13](https://github.com/revenium/revenium-metering-python/issues/13)) ([9cdd1e8](https://github.com/revenium/revenium-metering-python/commit/9cdd1e840e190537e239a4df8f6639428a12f5d2))
* **internal:** expand CI branch coverage ([35018f6](https://github.com/revenium/revenium-metering-python/commit/35018f63bf80dc67bf648ea2c8de0c429e8b3711))
* **internal:** reduce CI branch coverage ([89839be](https://github.com/revenium/revenium-metering-python/commit/89839be4e495cecbf82241e9e1bf6f7f2ee29cb3))
* **internal:** remove extra empty newlines ([#11](https://github.com/revenium/revenium-metering-python/issues/11)) ([bccf0e9](https://github.com/revenium/revenium-metering-python/commit/bccf0e9e8ce617911786d1ff250f2dbd50b7e767))
* **internal:** remove trailing character ([#68](https://github.com/revenium/revenium-metering-python/issues/68)) ([515595b](https://github.com/revenium/revenium-metering-python/commit/515595bdc17bb7d6d45f01e15659158cc6e09a37))
* **internal:** slight transform perf improvement ([#77](https://github.com/revenium/revenium-metering-python/issues/77)) ([87708ac](https://github.com/revenium/revenium-metering-python/commit/87708ac803aeffd8f0d464ac2aaefe57746ad873))
* **tests:** improve enum examples ([#79](https://github.com/revenium/revenium-metering-python/issues/79)) ([0e64dd8](https://github.com/revenium/revenium-metering-python/commit/0e64dd8d839cb344c51141831b591a2db25ec4df))
* update SDK settings ([#3](https://github.com/revenium/revenium-metering-python/issues/3)) ([350ae32](https://github.com/revenium/revenium-metering-python/commit/350ae32a7b5ec7cc98c8da08f590e486f4492769))

## 4.0.0 (2025-04-10)

Full Changelog: [v3.2.2...v4.0.0](https://github.com/revenium/revenium-metering-python/compare/v3.2.2...v4.0.0)

### Features

* **api:** api update ([9cc4756](https://github.com/revenium/revenium-metering-python/commit/9cc47568f745453fdff63863ebfd69b2d3579895))
* **api:** api update ([02e77f5](https://github.com/revenium/revenium-metering-python/commit/02e77f57d2544ede9d0c3eb40e01744a685b3119))
* **api:** api update ([b6c84d9](https://github.com/revenium/revenium-metering-python/commit/b6c84d91b2b647d449129df6ce22c7ba94f5e0c1))
* **api:** api update ([edb7ea8](https://github.com/revenium/revenium-metering-python/commit/edb7ea8cad54dc36611d9b1d9d29e624c5d3cf2d))

## 3.2.2 (2025-04-10)

Full Changelog: [v3.2.1...v3.2.2](https://github.com/revenium/revenium-metering-python/compare/v3.2.1...v3.2.2)

### Chores

* **internal:** expand CI branch coverage ([35018f6](https://github.com/revenium/revenium-metering-python/commit/35018f63bf80dc67bf648ea2c8de0c429e8b3711))
* **internal:** reduce CI branch coverage ([89839be](https://github.com/revenium/revenium-metering-python/commit/89839be4e495cecbf82241e9e1bf6f7f2ee29cb3))
* **internal:** slight transform perf improvement ([#77](https://github.com/revenium/revenium-metering-python/issues/77)) ([87708ac](https://github.com/revenium/revenium-metering-python/commit/87708ac803aeffd8f0d464ac2aaefe57746ad873))
* **tests:** improve enum examples ([#79](https://github.com/revenium/revenium-metering-python/issues/79)) ([0e64dd8](https://github.com/revenium/revenium-metering-python/commit/0e64dd8d839cb344c51141831b591a2db25ec4df))

## 3.2.1 (2025-04-07)

Full Changelog: [v3.1.0...v3.2.1](https://github.com/revenium/revenium-metering-python/compare/v3.1.0...v3.2.1)

### Features

* **api:** api update ([#70](https://github.com/revenium/revenium-metering-python/issues/70)) ([f3ef651](https://github.com/revenium/revenium-metering-python/commit/f3ef6510eb17cfd51beee437bb8b13a337dfbd2b))
* **api:** api update ([#72](https://github.com/revenium/revenium-metering-python/issues/72)) ([4211732](https://github.com/revenium/revenium-metering-python/commit/42117321009bd3eacdf80e51a5bb0f8ad59686f5))
* **api:** api update ([#73](https://github.com/revenium/revenium-metering-python/issues/73)) ([37572c1](https://github.com/revenium/revenium-metering-python/commit/37572c1d62635929861fffe62834f4cc87a3bd22))
* **api:** api update ([#74](https://github.com/revenium/revenium-metering-python/issues/74)) ([70ae4ff](https://github.com/revenium/revenium-metering-python/commit/70ae4ffff64bbc9be29ecb81afcbd4d96bc41e90))
* **api:** api update ([#75](https://github.com/revenium/revenium-metering-python/issues/75)) ([cc83c06](https://github.com/revenium/revenium-metering-python/commit/cc83c06a0e8b26a342f2df4940db98c16551a7e1))

## 3.1.0 (2025-04-04)

Full Changelog: [v3.0.0...v3.1.0](https://github.com/revenium/revenium-metering-python/compare/v3.0.0...v3.1.0)

### Features

* **api:** api update ([#65](https://github.com/revenium/revenium-metering-python/issues/65)) ([4940606](https://github.com/revenium/revenium-metering-python/commit/494060672f8339627f2594d983f3289581754c12))
* **api:** api update ([#67](https://github.com/revenium/revenium-metering-python/issues/67)) ([56f305e](https://github.com/revenium/revenium-metering-python/commit/56f305eed29a2344e33664b676d12352902be00d))


### Chores

* **internal:** remove trailing character ([#68](https://github.com/revenium/revenium-metering-python/issues/68)) ([515595b](https://github.com/revenium/revenium-metering-python/commit/515595bdc17bb7d6d45f01e15659158cc6e09a37))

## 3.0.0 (2025-04-01)

Full Changelog: [v2.4.0...v3.0.0](https://github.com/revenium/revenium-metering-python/compare/v2.4.0...v3.0.0)

### Features

* **api:** api update ([#62](https://github.com/revenium/revenium-metering-python/issues/62)) ([c790527](https://github.com/revenium/revenium-metering-python/commit/c79052789cd70eaee8171c09d0cfedb5a2e3bda5))

## 2.4.0 (2025-04-01)

Full Changelog: [v2.3.0...v2.4.0](https://github.com/revenium/revenium-metering-python/compare/v2.3.0...v2.4.0)

### Features

* **api:** api update ([#59](https://github.com/revenium/revenium-metering-python/issues/59)) ([7861dc4](https://github.com/revenium/revenium-metering-python/commit/7861dc4dde3675b297c37aed7b9e67c883857dfe))

## 2.3.0 (2025-04-01)

Full Changelog: [v2.2.0...v2.3.0](https://github.com/revenium/revenium-metering-python/compare/v2.2.0...v2.3.0)

### Features

* **api:** api update ([#56](https://github.com/revenium/revenium-metering-python/issues/56)) ([5c06d9e](https://github.com/revenium/revenium-metering-python/commit/5c06d9e608c0a1843585b97151780e1f6a96d9a7))

## 2.2.0 (2025-03-28)

Full Changelog: [v2.1.0...v2.2.0](https://github.com/revenium/revenium-metering-python/compare/v2.1.0...v2.2.0)

### Features

* **api:** api update ([#50](https://github.com/revenium/revenium-metering-python/issues/50)) ([a341880](https://github.com/revenium/revenium-metering-python/commit/a34188079797aabad5ca3a8bffcc5105d4fa20c9))
* **api:** api update ([#52](https://github.com/revenium/revenium-metering-python/issues/52)) ([588453e](https://github.com/revenium/revenium-metering-python/commit/588453e52c8b990e1d49dd8ff3254176269f6cd3))
* **api:** api update ([#53](https://github.com/revenium/revenium-metering-python/issues/53)) ([35a5649](https://github.com/revenium/revenium-metering-python/commit/35a56490fe0b5fcc056a64de4d2a4ddc53bfea38))
* **api:** api update ([#54](https://github.com/revenium/revenium-metering-python/issues/54)) ([eca927e](https://github.com/revenium/revenium-metering-python/commit/eca927e776f763abe944064874c7ca0a0decd244))

## 2.1.0 (2025-03-28)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/revenium/revenium-metering-python/compare/v2.0.0...v2.1.0)

### Features

* **api:** api update ([#47](https://github.com/revenium/revenium-metering-python/issues/47)) ([fbaf56d](https://github.com/revenium/revenium-metering-python/commit/fbaf56d8b5a17b1ae394ea153190b1e9e2aaadcf))

## 2.0.0 (2025-03-28)

Full Changelog: [v1.4.1...v2.0.0](https://github.com/revenium/revenium-metering-python/compare/v1.4.1...v2.0.0)

### Features

* **api:** api update ([#41](https://github.com/revenium/revenium-metering-python/issues/41)) ([9ed8e89](https://github.com/revenium/revenium-metering-python/commit/9ed8e892ddd1f46bea22fe2df02aaccf881f96b9))
* **api:** api update ([#43](https://github.com/revenium/revenium-metering-python/issues/43)) ([4253f04](https://github.com/revenium/revenium-metering-python/commit/4253f04928d9d188e819911a203b852863d99970))
* **api:** api update ([#44](https://github.com/revenium/revenium-metering-python/issues/44)) ([3b3989a](https://github.com/revenium/revenium-metering-python/commit/3b3989a9b9a5deb03945241dd773d20466219265))
* **api:** api update ([#45](https://github.com/revenium/revenium-metering-python/issues/45)) ([e0edf27](https://github.com/revenium/revenium-metering-python/commit/e0edf27d7fb7eaa274a60b1cb90c06ec19384b23))

## 1.4.1 (2025-03-27)

Full Changelog: [v1.4.0...v1.4.1](https://github.com/revenium/revenium-metering-python/compare/v1.4.0...v1.4.1)

### Chores

* fix typos ([#38](https://github.com/revenium/revenium-metering-python/issues/38)) ([719f112](https://github.com/revenium/revenium-metering-python/commit/719f11225e758eea6a1ae25b404040e4a853184b))

## 1.4.0 (2025-03-20)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/revenium/revenium-metering-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** api update ([#34](https://github.com/revenium/revenium-metering-python/issues/34)) ([d532f96](https://github.com/revenium/revenium-metering-python/commit/d532f9606c202832668d360d8a1fc7fe0d9e155a))
* **api:** api update ([#36](https://github.com/revenium/revenium-metering-python/issues/36)) ([c103db2](https://github.com/revenium/revenium-metering-python/commit/c103db2857567438cfc1154388134e6a3abf0f57))

## 1.3.0 (2025-03-20)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/revenium/revenium-metering-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** api update ([#28](https://github.com/revenium/revenium-metering-python/issues/28)) ([af3f4f4](https://github.com/revenium/revenium-metering-python/commit/af3f4f43d57b478323acdc8d590cbbfa7ab8deda))
* **api:** api update ([#30](https://github.com/revenium/revenium-metering-python/issues/30)) ([56602fe](https://github.com/revenium/revenium-metering-python/commit/56602feec4cb371b126d89b7a3b7bcb173b8bfe8))
* **api:** api update ([#31](https://github.com/revenium/revenium-metering-python/issues/31)) ([b042007](https://github.com/revenium/revenium-metering-python/commit/b042007eca5954e9eaea93eeec9120a9f4f0e6e7))
* **api:** api update ([#32](https://github.com/revenium/revenium-metering-python/issues/32)) ([fec56ca](https://github.com/revenium/revenium-metering-python/commit/fec56ca89ce68cf98ee88c7f4fa283f9ed708b9c))

## 1.2.0 (2025-03-20)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/revenium/revenium-metering-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** api update ([#25](https://github.com/revenium/revenium-metering-python/issues/25)) ([77334f1](https://github.com/revenium/revenium-metering-python/commit/77334f1f77b0f6ce3df41442f2037bb37e8d3dbf))

## 1.1.0 (2025-03-17)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/revenium/revenium-metering-python/compare/v1.0.1...v1.1.0)

### Features

* **api:** api update ([#21](https://github.com/revenium/revenium-metering-python/issues/21)) ([206dd6c](https://github.com/revenium/revenium-metering-python/commit/206dd6c2b49088eea94614750fd97c067db70b76))


### Bug Fixes

* **ci:** remove publishing patch ([#22](https://github.com/revenium/revenium-metering-python/issues/22)) ([a11a87b](https://github.com/revenium/revenium-metering-python/commit/a11a87b12a6e95e294e22d9037fafd93113b0961))

## 1.0.1 (2025-03-17)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/revenium/revenium-metering-python/compare/v1.0.0...v1.0.1)

### Bug Fixes

* **ci:** ensure pip is always available ([#18](https://github.com/revenium/revenium-metering-python/issues/18)) ([c92a6a3](https://github.com/revenium/revenium-metering-python/commit/c92a6a3430a507462b2d70a37dcc4525407faacb))

## 1.0.0 (2025-03-16)

Full Changelog: [v0.1.0-alpha.1...v1.0.0](https://github.com/revenium/revenium-metering-python/compare/v0.1.0-alpha.1...v1.0.0)

### Features

* **api:** update via SDK Studio ([#16](https://github.com/revenium/revenium-metering-python/issues/16)) ([fda738b](https://github.com/revenium/revenium-metering-python/commit/fda738b99aa121b04df02a64987f8d003ef8055e))


### Bug Fixes

* **types:** handle more discriminated union shapes ([#15](https://github.com/revenium/revenium-metering-python/issues/15)) ([63317f4](https://github.com/revenium/revenium-metering-python/commit/63317f448fbe4590a19d82ba5c67da7be0a6c4ab))


### Chores

* **internal:** bump rye to 0.44.0 ([#14](https://github.com/revenium/revenium-metering-python/issues/14)) ([614dbd4](https://github.com/revenium/revenium-metering-python/commit/614dbd4639c6ea18b16f91517bf91699562d5777))
* **internal:** codegen related update ([#13](https://github.com/revenium/revenium-metering-python/issues/13)) ([9cdd1e8](https://github.com/revenium/revenium-metering-python/commit/9cdd1e840e190537e239a4df8f6639428a12f5d2))
* **internal:** remove extra empty newlines ([#11](https://github.com/revenium/revenium-metering-python/issues/11)) ([bccf0e9](https://github.com/revenium/revenium-metering-python/commit/bccf0e9e8ce617911786d1ff250f2dbd50b7e767))

## 0.1.0-alpha.1 (2025-03-13)

Full Changelog: [v0.0.1-alpha.2...v0.1.0-alpha.1](https://github.com/revenium/revenium-metering-python/compare/v0.0.1-alpha.2...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([#8](https://github.com/revenium/revenium-metering-python/issues/8)) ([f68c95f](https://github.com/revenium/revenium-metering-python/commit/f68c95fed3c81e362a017a16677ea7b1af9b4aea))

## 0.0.1-alpha.2 (2025-03-11)

Full Changelog: [v0.0.1-alpha.1...v0.0.1-alpha.2](https://github.com/revenium/revenium-metering-python/compare/v0.0.1-alpha.1...v0.0.1-alpha.2)

## 0.0.1-alpha.1 (2025-03-10)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/revenium/revenium-metering-python/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* go live ([#1](https://github.com/revenium/revenium-metering-python/issues/1)) ([65fd84b](https://github.com/revenium/revenium-metering-python/commit/65fd84ba27271c5e68054e8f4e5290e3e6cb339f))
* update SDK settings ([#3](https://github.com/revenium/revenium-metering-python/issues/3)) ([350ae32](https://github.com/revenium/revenium-metering-python/commit/350ae32a7b5ec7cc98c8da08f590e486f4492769))
